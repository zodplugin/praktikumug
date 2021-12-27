# Fungsi treeHeight(tree) untuk menghitung tinggi level tree
def treeHeight(tree):
    # [1] Memastikan apakah tree kosong, jika kosong maka kembalikan nilai 0
    if tree is None:
        return 0

    # [2] Cari tinggi subtree kiri dengan memanggil fungsi ini secara rekursif 
    # dengan argument root dari subtree kiri.
    leftTree = treeHeight(tree.left)
    # [3] Cari tinggi subtree kanan dengan memanggil rekursif fungsi ini 
    # dengan argument root dari subtree kanan.
    rightTree = treeHeight(tree.right)
    # [4] Bandingkan tinggi subtree kiri dan kanan, kembalikan nilai tertinggi dari keduanya + 1.
    # Kita menambahkan 1 untuk menambahkan level root.
    return max(leftTree,rightTree) + 1
    
    
