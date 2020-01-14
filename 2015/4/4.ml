
let input = "yzbqklnj"

let first n s = String.sub s 0 n
let postpend pre s = pre ^ s

let rec churn i =
    let s = i |> string_of_int |> ((^) input) |> Digest.string |> Digest.to_hex |> first 6 in
    if s = "000000" then i else churn (i+1)
        
