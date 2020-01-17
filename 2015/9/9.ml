
module M = Map.Make(String)
module S = Set.Make(String)

let ic = open_in "9/input"

let rec rl acc ic = match input_line ic with | s -> rl (s::acc) ic | exception End_of_file -> acc

let lines = rl [] ic

let parse line = Scanf.sscanf line "%s to %s = %d" (fun a b c -> (a,b,c))

let sed = List.rev_map parse lines

let nodes = List.fold_left (fun set (s,e,_) -> S.add s (S.add e set)) S.empty sed
let edges = List.fold_left (fun m (s,e,d) -> let m' = M.add s (M.add e d (M.find s m)) m  in
                                            M.add e (M.add s d (M.find e m')) m')
                            (S.fold (fun n m-> M.add n M.empty m) nodes M.empty)
                            sed

let rec permute l =
    let rec interleave x lst =
        match lst with
        | [] -> [[x]]
        | h::t -> (x::lst) :: (List.map (fun y -> h::y) (interleave x t))
    in match l with
    | h::t -> List.concat (List.map (interleave h) (permute t))
    | _ -> [l]

let perms = permute (S.elements nodes)

let dist s e = match s with | None -> 0 | Some s -> M.find e (M.find s edges)

let totals = List.map (fun l -> let _, tot = List.fold_left (fun (s,d) e -> (Some e,d+(dist s e))) (None,0) l in tot) perms

let ans = List.sort_uniq (-) totals
let ans2 = List.rev ans

                                


let () = close_in ic

