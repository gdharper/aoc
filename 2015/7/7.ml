
let ic = open_in "7/input"

let o x y = (x lor y) land 0xffff
let a x y = (x land y) land 0xffff
let n x = (lnot x) land 0xffff
let ls x n = (x lsl n) land 0xffff
let rs x n = x lsr n

let rec rl ic acc = match input_line ic with | s -> rl ic (s::acc) | exception End_of_file -> acc

let lines = rl ic []

type wire = Val of int
    | Pass of string
    | Or of string * string
    | And of string * string
    | Ls of string * int
    | Rs of string * int
    | Not of string

module M = Map.Make(String)

let parse line =
    if String.contains line 'D' then
        Scanf.sscanf line "%s AND %s -> %s" (fun a b c -> (c, And (a,b)))
    else if String.contains line 'L' then
        Scanf.sscanf line "%s LSHIFT %u -> %s" (fun a b c -> (c, Ls (a,b)))
    else if String.contains line 'N' then
        Scanf.sscanf line "NOT %s -> %s" (fun a b -> (b, Not a))
    else if String.contains line 'O' then
        Scanf.sscanf line "%s OR %s -> %s" (fun a b c -> (c, Or (a,b)))
    else if String.contains line 'R'then
        Scanf.sscanf line "%s RSHIFT %u -> %s" (fun a b c -> (c, Rs (a,b)))
    else
        try
            Scanf.sscanf line "%u -> %s" (fun a b -> (b, Val a))
        with _ ->
            Scanf.sscanf line "%s -> %s" (fun a b -> (b, Pass a))

let m = List.fold_left (fun m l -> let (s,w) = parse l in M.add s w m) (M.singleton "1" ( Val 1)) lines

let rec eval m k = 
    match M.find k m with
    | Val i -> (m, i)
    | Pass s -> let m,i = eval m s in ((M.add k (Val i) m), i)
    | Or (x,y) -> let m,x = eval m x in let m,y = eval m y in let i = o x y in ((M.add k (Val i) m), i)
    | And (x,y) -> let m,x = eval m x in let m,y = eval m y in let i = a x y in ((M.add k (Val i) m), i)
    | Ls (s,n) -> let m,i = eval m s in let i = ls i n in ((M.add k (Val i) m), i)
    | Rs (s,n) -> let m,i = eval m s in let i = rs i n in ((M.add k (Val i) m), i)
    | Not s -> let m', i = eval m s in let i = n i in ((M.add k (Val i) m), i)

let _,ans = eval m "a"

let m = M.add "b" (Val ans) m

let _, ans2 = eval m "a"

let () = close_in ic


