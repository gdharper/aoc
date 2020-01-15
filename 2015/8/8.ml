
let ic = open_in "8/input"

let rec rl acc ic = match input_line ic with | s -> rl (s::acc) ic | exception End_of_file -> acc

let lines = rl [] ic

let consume n s = String.sub s n (String.length s - n)

let parse line =
    let count = String.length line in
    let rec p n s =
        match String.index_opt s '\\' with
        | None -> n
        | Some i -> (match s.[i+1] with
            | '"'
            | '\\' -> p (n+1) (consume (i+2) s)
            | 'x' -> p (n+3) (consume (i+4) s)
            | _ -> print_string line; print_newline (); failwith "AHHH")
    in (count, count - (p 2 (String.sub line 1 (String.length line - 2))))

let vals = List.rev_map parse lines

let code, mem = List.fold_left (fun (a,b) (c,d) -> (a+c, b+d)) (0,0) vals

let ans = code - mem

let parse2 line =
    let count = String.length line in
    let rec p n s =
        match String.index_opt s '\\' with
        | None -> n
        | Some i -> (match s.[i+1] with
            | '"'
            | '\\' -> p (n+2) (consume (i+2) s)
            | 'x' -> p (n+1) (consume (i+4) s)
            | _ -> print_string line; print_newline (); failwith "AHHH")
    in (count, count + (p 4 (String.sub line 1 (String.length line - 2))))

let vals2 = List.rev_map parse2 lines

let code2, mem2 = List.fold_left (fun (a,b) (c,d) -> (a+c, b+d)) (0,0) vals2

let ans2 = mem2 - code2


let () = close_in ic

