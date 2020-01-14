
let ic = open_in "6/input"

let rec rl ic acc = match input_line ic with | l -> rl ic (l::acc) | exception End_of_file -> acc

let lines = rl ic []

let () = close_in ic

let lights = Array.make_matrix 1000 1000 0

type ins = On of  int * int * int * int | Off of  int * int * int * int | Tog of  int * int * int * int

let on s = Scanf.sscanf s "turn on %d,%d through %d,%d" (fun a b c d -> On (a,b,c,d))

let off s = Scanf.sscanf s "turn off %d,%d through %d,%d" (fun a b c d -> Off (a,b,c,d))

let tog s = Scanf.sscanf s "toggle %d,%d through %d,%d" (fun a b c d -> Tog (a,b,c,d))

let parse line =
    match String.sub line 6 1 with
    | "n" -> on line
    | "f" -> off line
    | " " -> tog line
    | _ -> failwith "ADDDDDD"

let instructions = List.rev_map parse lines

let set a b c d boo =
    for i = a to c do
        for j = b to d do
            let v = lights.(i).(j) in 
            let v' = if boo then v + 1 else (if v > 0 then v -1 else 0) in
            lights.(i).(j) <- v'
        done
    done

let toggle a b c d =
    for i = a to c do
        for j = b to d do
            let v = lights.(i).(j) + 2 in
            lights.(i).(j) <- v
        done
    done

let rec work i = 
    if i = [] then () else
    let h::t = i in
    match h with
    | On (a,b,c,d) -> set a b c d true; work t
    | Off (a,b,c,d) -> set a b c d false; work t
    | Tog (a,b,c,d) -> toggle a b c d; work t

let () = work instructions

let sum = Array.fold_left (fun sum a -> sum + (Array.fold_left (fun sum' b -> sum' + b) 0 a)) 0 lights


