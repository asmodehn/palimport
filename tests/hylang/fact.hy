(require [hy.contrib.loop [loop]])

(defn factorial [n]
  (loop [[i n] [acc 1]]
    (if (zero? i)
      acc
      (recur (dec i) (* acc i)))))

;; Test
;; (factorial 1000)