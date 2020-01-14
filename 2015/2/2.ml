
let load_lines path =
    let ic = open_in path in
    let rec rl ic acc = match input_line ic with | l -> (rl ic (l::acc)) | exception _ -> acc in
    let lines = rl ic [] in
    close_in ic;
    List.rev lines

let lines = load_lines "input" |> List.rev_map (String.split_on_char 'x')
let sides = List.rev_map (List.map int_of_string) lines

let paper l = match l with
    |[a;b;c] -> 
        let s1 = a * b in
        let s2 = a * c in
        let s3 = b * c in
        2 * (s1 + s2 + s3) + (min s1 (min s2 s3))
    | _ -> failwith "PAAPER"

let ribbon l = match l with
    |[a;b;c] -> 2 * (a + b + c - (max a (max b c))) + (a * b * c)
    |_ -> failwith "RIBBOOON"

let totp = sides |> List.rev_map paper |> List.fold_left (+) 0
let totr = sides |> List.rev_map ribbon |> List.fold_left (+) 0


