def isRepresented(query: str, wlist: [str]) -> bool:
    result = False
    prev_candidates = [[0]]
    next_candidates = []
    while len(prev_candidates)>0:
        for c in prev_candidates:
            for w in wlist:
                if query[max(c):].startswith(w):
                    next_candidates.append(c+[max(c)+len(w)])
        for n in next_candidates:      
            if query[max(n):]=="":
                # print(f'Candidate passed: {n}')
                result = True
                split_solution = " ".join([query[n[i]:n[i+1]] for i in range(len(n)-1)])
                print(f"Solution found: {split_solution}")
        prev_candidates = [i for i in next_candidates if max(i)<len(query)]
        next_candidates = []
    return result
