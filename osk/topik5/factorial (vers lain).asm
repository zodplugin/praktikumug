   
; File: factorial.asm
;
; Program ini menghitung nilai factorial dari angka yang dimasukkan user (0 s.d 10)
;

%include "asm_io.inc"

segment .data
;
; Output strings
;
prompt          db    	"Masukkan angka (0 s.d 10): ", 0
err_msg			db		"Angka yang Anda masukkan tidak diantara 0 s.d 10" , 0

segment .bss


segment .text
        global  _main
_main:
        enter   0,0               ; setup routine
        pusha

		
		; Prompt user untuk memasukkan angka 0 s.d 10
		 mov eax, prompt
      		 call print_string
      		 call read_int
				
		; bandingkan eax dengan 10 desimal, jika eax > 10 lompat ke error		
		cmp eax, 10
      		jg error
		
		; bandingkan eax dengan 0 desimal, jika eax < 0 lompat ke error
		cmp eax, 0
      		jl error

		
		; jika nilai yang dimasukkan = 0, lompat ke nol_faktorial
		cmp eax, 0
     		je nol_faktorial

                ; Persiapkan register untuk loop
		; ECX sebagai counter dari loop dan EAX sebagai hasil dari faktorial
		; EAX = EAX * ECX
		mov ecx, eax
	        sub ecx, 1
		


; Loop:
; while ECX > 0, EAX = EAX * ECX
; ECX--
loop_start:
mul ecx
sub ecx ,1
cmp ecx, 0
jg loop_start
call print_int
jmp end


; block kode untuk menghitung 0! = 1
nol_faktorial:
mov eax, 1
call print_int
jmp end


; block kode untuk menampilkan error jika angka yang dimasukkan bukan 0 s.d 10
error:
mov eax, err_msg
call print_string


; akhir dari program
end: 

		popa
        mov     eax, 0            ; return back to C
        leave                     
        ret