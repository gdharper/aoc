
let input = "vzbxkghb"

type c = A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z

let c_of = function
    |'a' -> A
    |'b' -> B
    |'c' -> C
    |'d' -> D
    |'e' -> E
    |'f' -> F
    |'g' -> G
    |'h' -> H
    |'i' -> I
    |'j' -> J
    |'k' -> K
    |'l' -> L
    |'m' -> M
    |'n' -> N
    |'o' -> O
    |'p' -> P
    |'q' -> Q
    |'r' -> R
    |'s' -> S
    |'t' -> T
    |'u' -> U
    |'v' -> V
    |'w' -> W
    |'x' -> X
    |'y' -> Y
    |'z' -> Z
    | c -> failwith (Char.escaped c)

let rec to_c s =
    if s = "" then [] else
        (c_of s.[0])::(to_c (String.sub s 1 (String.length s - 1)))


let next = function
    |A -> B
    |B -> C
    |C -> D
    |D -> E
    |E -> F
    |F -> G
    |G -> H
    |H -> I
    |I -> J
    |J -> K
    |K -> L
    |L -> M
    |M -> N
    |N -> O
    |O -> P
    |P -> Q
    |Q -> R
    |R -> S
    |S -> T
    |T -> U
    |U -> V
    |V -> W
    |W -> X
    |X -> Y
    |Y -> Z
    |Z -> A

let inc l =
    let rec i = function
        | Z::t -> A::(i t)
        | h::t -> (next h)::t
        | [] -> []
    in List.rev (i (List.rev l))

let rec seq3 =function
    | []
    | [_]
    | [_;_] -> false
    | h::h'::h''::t  ->
        if h <> Z && h' <> Z && h' = (next h) && h'' = (next h') then true
        else seq3 (h'::h''::t)

let no_bad = List.for_all (fun c -> c <> I && c <> L && c <> O)

let rec dubs = function
    | []
    | [_] -> 0
    | h::h'::t -> if h = h' then 1 + (dubs t) else dubs (h'::t)


let good l = seq3 l && (no_bad l) && (dubs l > 1)

let rec spin l = 
    if good l then l
    else spin (inc l)


let ans = spin (to_c input)
let ans2 = spin (inc ans)
























