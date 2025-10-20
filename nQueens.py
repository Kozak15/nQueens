import itertools
def check(s):#Takes in a string of numbers
    for i in range(len(s)):
            for j in range(i+1 ,len(s)):
                if abs(int(s[i]) - int(s[j])) == abs(j - i):
                    return False
    return True
#A solution is represented by a string. Say
#First character is 1, there is a queen on A1
full_list_of_solutions = [
    '15863724', '16837425', '17468253', '17582463', '24683175', 
    '25713864', '25741863', '26174835', '26831475', '27368514',
    '27581463', '28613574', '31758246', '35281746', '35286471', 
    '35714286', '35841726', '36258174', '36271485', '36275184',
    '36418572', '36428571', '36814752', '36815724', '36824175', 
    '37285146', '37286415', '38471625', '41582736', '41586372',
    '42586137', '42736815', '42736851', '42751863', '42857136', 
    '42861357', '46152837', '46827135', '46831752', '47185263',
    '47382516', '47526138', '47531682', '48136275', '48157263', 
    '48531726', '51468273', '51842736', '51863724', '52468317',
    '52473861', '52617483', '52814736', '53168247', '53172864', 
    '53847162', '57138642', '57142863', '57248136', '57263148',
    '57263184', '57413862', '58413627', '58417263', '61528374', 
    '62713584', '62714853', '63175824', '63184275', '63185247',
    '63571428', '63581427', '63724815', '63728514', '63741825', 
    '64158273', '64285713', '64713528', '64718253', '68241753',
    '71386425', '72418536', '72631485', '73168524', '73825164',
    '74258136', '74286135', '75316824', '82417536', '82531746',
    '83162574', '84136275'
]
def rotate_90(s,n):
    ans = ""
    lst = list(s)
    for i in range(1 , len(lst)+1):
        ans += str(n- lst.index(str(i)))
    return ans
def rotate_180(s,n):
    return rotate_90(rotate_90(s,n),n)
def rotate_270(s,n):
    return rotate_90(rotate_180(s,n),n)
    #rotate_90(rotate_180(s)) works as well but its less funny
def reflect(s,n):
    ans = ""
    for tn in s:
        ans += str(n+1 - int(tn))
    return ans
def check_equiv(s1 , s2):
    ref = reflect(s1, n)
    return any(s2 == t
        for t in [rotate_90(s1, n),rotate_180(s1, n),rotate_270(s1, n),ref,
                rotate_90(ref, n),rotate_180(ref, n),rotate_270(ref, n),])
    
simple_list_of_solutions = ['15863724', '16837425', '24683175', '25713864', 
                            '25741863', '26174835', '26831475', '27368514', 
                            '27581463', '35281746', '35841726', '36258174'] 
def solveNqueens(n):#for 1<= n <= 9. I will upload no restrictions in the future
    s,lst = ''.join([str(i) for i in range(1,n+1)]),[]
    for item in itertools.permutations(s):
        ans = ''.join(item)
        if check(ans):
            if not any(val in lst for val in [ans,rotate90(ans,n),rotate180(ans,n),rotate270(ans,n)]):
                lst.append(ans)      
    return lst,len(lst)


