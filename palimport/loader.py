
import filefinder2

from palimport._utils import _verbose_message


class Loader(filefinder2.machinery.SourceFileLoader):
    """
    Loader base class for a sourcefile in a custom langauge.
    Currently supported parsers :
     - lark

    To define you own loader, you should extend this class
    """

    parser = None  # mandatory class member. Need to be defined by any derived class
    transformer = None  # mandatory class member. Need to be defined by any derived class

    # def get_code(self, fullname):
    #     source = self.get_source(fullname)
    #     _verbose_message('parsing code for "{0}"'.format(fullname))
    #     try:
    #         ast = self.source_to_ast(source, self.get_filename(fullname))
    #         _verbose_message('compiling code for "{0}"'.format(fullname))
    #         code = self.ast_to_code(ast, self.get_filename(fullname))
    #         return code
    #     except TypeError:
    #         raise

    # We avoid overriding get_source here to not have to deal with decode_source() if we can avoid it

    def get_code(self, fullname):
        try:
            source = self.get_source(fullname)
        except Exception:
            print("LarkLoader get_code Exception")
            raise

        _verbose_message('transforming code for "{0}"'.format(fullname))

        parsed_source = self.parser.parse(source)
        transformed_source = self.transformer.transform(parsed_source)

        _verbose_message('compiling code for "{0}"'.format(fullname))
        try:
            code = self.source_to_code(transformed_source, self.get_filename(fullname))
            return code
        except TypeError:
            raise

    def source_to_code(self, data, path):
        """Return the code object compiled from source.
        The 'data' argument can be any object type that compile() supports.
        """
        return compile(data, path, 'exec', dont_inherit=True)

    # def source_to_ast(self, data, path):
    #     _verbose_message('parsing code in "{0}"'.format(path))
    #     return self.lark.parse(data)
    #
    # def ast_to_code(self, ast, path):
    #     pysource = interpret(ast)
    #     return self.source_to_code(pysource, path)
