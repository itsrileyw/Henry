servers = {
"BESTMETA":"272178393091407872",
"GOAT":"263157828242505729"
}
channels = {
"BESTMETA_GENERAL":"454473643020517379",
"BESTMETA_HENRYS_V2":"477242374469451817",
"GOAT_GENERAL":"263157828242505729",
}
chain = [
servers["BESTMETA"],channels["BESTMETA_HENRYS_V2"],
servers["GOAT"],channels["GOAT_GENERAL"],
]

list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(0, int(len(list)),2):
    print(list[i], list[i+1])