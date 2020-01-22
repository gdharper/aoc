

let input = "3113322113"

let listize i = 
    let intchar = function
        | '0' -> 0
        | '1' -> 1
        | '2' -> 2
        | '3' -> 3
        | '4' -> 4
        | '5' -> 5
        | '6' -> 6
        | '7' -> 7
        | '8' -> 8
        | '9' -> 9
    in let i = List.init (String.length i) (String.get i)
    in List.map intchar i

let input = listize input

let rec parse inp n c outp =
    match inp with
    | [] -> c::n::outp
    | h::t -> parse t (if c = h then n+1 else 1) h (if c = h then outp else c::n::outp)

let rec rep n i =
    if n < 1 then i
    else
        let h::t = i in
        rep (n-1) (List.rev (parse t 1 h []))

