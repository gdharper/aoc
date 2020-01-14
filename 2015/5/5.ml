
let load_lines path =
    let ic = open_in path in
    let rec rl ic acc = match input_line ic with | l -> (rl ic (l::acc)) | exception _ -> acc in
    let lines = rl ic [] in
    close_in ic;
    List.rev lines

let lines = load_lines "5/input"

let consume n s = String.sub s n ((String.length s) - n)

let has_vows s =
    let rec f acc s =
        if s = "" || acc >= 3 then acc
        else match String.get s 0 with
            |'a'|'e'|'i'|'o'| 'u' -> (f (acc+1) (consume 1 s))
            | _ -> (f acc (consume 1 s))
    in (f 0 s) = 3

let has_dub n s=
    let rec f s c =
        if String.length s < (n+1) then false
        else if (String.get s n) = c then true
        else f (consume 1 s) (String.get s 0)
    in (f (consume 1 s) (String.get s 0))

let rec has_bad s =
    if (String.length s) <= 1 then false else
    match String.get s 0 with
    | 'a' -> if String.get s 1 = 'b' then true
            else has_bad (consume 1 s)
    | 'c' -> if String.get s 1 = 'd' then true
            else has_bad (consume 1 s)
    | 'p' -> if String.get s 1 = 'q' then true
            else has_bad (consume 1 s)
    | 'x' -> if String.get s 1 = 'y' then true
            else has_bad (consume 1 s)
    | _ -> has_bad (consume 1 s)

(* Part 1 *)
let check line = has_vows line && (has_dub 0 line) && not (has_bad line)

let total = List.fold_left (fun acc line -> if check line then acc+1 else acc) 0 lines

(* Part 2 *)

module S = Set.Make(String);;

let has_pairs s =
    let rec twice ll l acc s =
        if String.length s < 2 then false else
        let p = String.sub s 0 2 in
        match S.find_opt p acc with
        | None -> twice l p (S.add p acc) (consume 1 s)
        | Some _ -> if l = p && ll <> p then twice l p acc (consume 1 s) else true
    in twice "" "" S.empty s

let check2 line = has_pairs line && (has_dub 1 line)
let total2 = List.fold_left (fun acc line -> if check2 line then acc+1 else acc) 0 lines







