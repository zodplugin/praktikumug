   ; directive include
%include "asm_io.inc"

segment .data
   ; directive Dx
   msg1 db 'Masukkan angka 1: ',0;
   msg2 db 'Masukkan angka 2: ',0;
   msg3 db 'Angka pertama yang Anda masukkan: ',0;
   msg4 db 0ah, 'Angka kedua yang Anda masukkan: ',0;
	
segment .bss
   ; directive RESx
   input resd 1;
   input2 resd 1;
segment .text
   global _main
   _main:
      ; Routine “setup”
      enter  0, 0
      pusha
      ; Program Anda di bawah
      
      mov   eax, msg1    ; taruh alamat memori variabel hello ke register eax
      call  print_string  ; 
      
      call read_int ; baca nilai integer dari user
      mov [input],eax ; 8 input ke memori dengan label 
      
      mov   eax, msg2    ; taruh alamat memori variabel hello ke register eax
      call  print_string  ; 
        
      call read_int ;
      mov [input2],eax;

      mov eax, msg3;
      call print_string ;

      mov eax,[input] ; pindahkan isi dari variabel input ke register eax
      call print_int ;

      mov eax, msg4;
      call print_string;

      mov eax,[input2] ;
      call print_int;


      ; Routine “cleanup”
      popa
      mov    eax, 0
      leave
      ret
      
