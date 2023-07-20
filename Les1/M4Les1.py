
# def strcounter(s): #решение за N**2
#     for sym in s: # abc
#         counter = 0
#         for sub_sym in s: # abc 
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)

# strcounter('aabc')

# def strcounter(s): # решение за N * M O(M*N) -> O(N^2)
#     for sym in set(s):  # bac  M - уник
#         counter = 0
#         for sub_sym in s:  # aab  N - уник
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)

# strcounter('aabbbbccd')

# commit

def strcounter(s): # abc O(N+M) -> O(N+M) -> O(2*N) -> O(N)
    syms_counter = {}
    for sym in s: # aab  N - все
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items(): # [(a, 2)(b, 1)] M - уник
        print(sym, count)
strcounter('aabbbbccd')