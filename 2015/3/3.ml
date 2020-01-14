

module Pair = struct
    type t = int * int
    let compare a b =
        let f = (fst a) - (fst b) in
        let s = (snd a) - (snd b) in
        if f <> 0 then f / (abs f)
        else if s <> 0 then s / (abs s)
        else 0
    end
        

module S = Set.Make (Pair)

let rec parse ic (x,y) (x',y') s s' b =
    if b then
        match input_char ic with
        | '>' -> parse ic ((x+1),y) (x',y') (S.add (x,y) s) s' (not b)
        | 'v' -> parse ic (x,(y-1)) (x',y') (S.add (x,y) s) s' (not b)
        | '<' -> parse ic ((x-1),y) (x',y') (S.add (x,y) s) s' (not b)
        | '^' -> parse ic (x,(y+1)) (x',y') (S.add (x,y) s) s' (not b)
        | _ -> failwith "AHHH"
        | exception End_of_file -> ((S.add (x,y) s),s')
    else
        match input_char ic with
        | '>' -> parse ic (x,y) ((x'+1),y') s (S.add (x',y') s') (not b)
        | 'v' -> parse ic (x,y) (x',(y'-1)) s (S.add (x',y') s') (not b)
        | '<' -> parse ic (x,y) ((x'-1),y') s (S.add (x',y') s') (not b)
        | '^' -> parse ic (x,y) (x',(y'+1)) s (S.add (x',y') s') (not b)
        | _ -> failwith "AHHH"
        | exception End_of_file -> (s,(S.add (x,y) s'))


let ic = open_in "input"

let s,s' = parse ic (0,0) (0,0) S.empty S.empty true

let () = close_in ic

let n = S.cardinal (S.union s s')

