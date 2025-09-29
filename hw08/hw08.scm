(define (ascending? s)
 (define (ascend x)
    (if (atom? x) x
        (if (null? (cdr x)) (car x)
            (let
                ((y (ascend (cdr x))))
                (if (number? y) 
                    (if (<= (car x) y) (car x) #f)
                    y
                ))))
 )
    (let
        ((result (ascend s)))
        (if (boolean? result) result #t)
    )
)

(define (my-filter pred s)
    (if (null? s) nil
        (if (pred (car s))
            (let ((x (car s))) (cons x (my-filter pred (cdr s))))
            (my-filter pred (cdr s)))
))

(define (interleave lst1 lst2) 
    (if (null? lst1)
        lst2
        (cons (car lst1) (interleave lst2 (cdr lst1)))
    )
)

; (define (no-repeats s)
;     (let
;         (
;             (safe_s (if (atom? s) (cons s nil) s))
;             (check_repeats
;                 (lambda (reps n) 
;                     (if (null? reps)
;                         #f 
;                         (if (not (= n (car reps))) (check_repeats (cdr reps) n) #t)
;                     )
;                 )
;             )
;         )
;         (if (null? safe_s) #t 
;             (if (check_repeats (cdr safe_s) (car safe_s))
;                 (no-repeats (cdr safe_s))
;                 (append (car safe_s) (no-repeats (cdr safe_s)))
;             )
;         )
;     )
; )

; try using helper function

(define (no-repeats s)
(define (nr s ulist ulist2)
        (if (null? s) nil
            (if (null? ulist2)
                (cons (car s) (nr (cdr s) (cons (car s) ulist) (cons (car s) ulist)))
                (if (= (car s) (car ulist2))
                    (nr (cdr s) ulist ulist)
                    (nr s ulist (cdr ulist2))))
        )
)
(nr s nil nil)
)