#Bài 1
A = [ 5 , 10 , 15 , 20 ]
print( A[0] , A[-1] )       
A.append(30)
A.insert(2 , 12)
A.remove(15)
A[1]= 99
print(A)
#Bài 2
B = {"apple" , "banana" , "cherry"}
B.add("orange")
B.add("banana")     #trong set vẫn chỉ có 1 banana
B.remove("apple")
if "mango" in B:
    print("có mango")
else:
    B.add("mango")
print(B)
#Bài 3
C = ( "Thứ 2" , "Thứ 3" , "Thứ 4" , "Thứ 5" , "Thứ 6")
print( C[0] , C[-1] )
C=list(C)
C.append("Funday")
C=tuple(C)
print(C)
#Bài 4
sinh_vien = [ "An" , "Bình" , "Chi" , "Dũng"]
sinh_vien.append( "Hà" )
sinh_vien.insert( 2, "Linh" )
sinh_vien.remove( "Chi" )
i = sinh_vien.index("Bình")
sinh_vien[i] = "Bình (đã cập nhật)"
print(sinh_vien)