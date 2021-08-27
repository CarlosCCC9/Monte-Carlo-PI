program exp_rand
implicit none
integer::i,con,j
real::f1(30),f2(30)
real::ventana
ventana=0.0000000001
open(1,file='poiss.dat',action='write',status='new')
open(2,file='vectores.dat',action='write',status='new')
do i=1,10
	do j=1,30
		f1(j)=0
		f2(j)=0
	end do
	call llena(f1,i)
	call llena(f2,1002-i)
	do j=1,30
		write(2,'(2f10.6)') f1(j),f2(j)
	end do
	con=0
	do j=1,30
		if( (f1(j)-f2(j)) < ventana) then
			con=con+1
		end if
	end do
	write(1,*) con
end do
close(1)
close(2)
end program

!subrutina que llena valores aleatorios
subroutine llena(f,j)
implicit none
integer::i,j
real::f(30),uni(30)
intent (in) j
intent(inout) f
call srand(j)
do i=1,30
	uni(i)=rand()
	f(i)=-log(1-uni(i))/2
end do
end subroutine
