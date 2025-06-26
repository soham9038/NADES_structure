c#################################################
c						 #
c program: Tetrahedral order parameter of water  #
c          around the protein                    #
c						 #
c#################################################
c============================================
c        Declare the variables              =
c============================================
      implicit none
      real * 8 x, y, z, d, r, xpos, ypos, zpos, t
      real * 8 dotpx, dotpy, dotpz, dotp, top, dotp1, w, angle
      integer i, j, k, n, m, p, q, s, line, a, ind, atom, resid
      integer line1, line2, line3, line4, atomi
      dimension r(5), xpos(5), ypos(5), zpos(5), p(5)
c---------------------------------------------------------------
c This dimensions depend on the number of waters present.      |
c Dimenion of "ind" is set according to the number of water    |
c present around the protein. All other dimensions are set     |
c according to the total number of water present in the system |
c---------------------------------------------------------------
      dimension x(10000), y(10000), z(10000), d(10000,10000), n(10000)
      dimension atom(10000), resid(10000), atomi(10000), ind(400)
c======================================================
c        Read the files required                      =
c======================================================
c     File containing atom-index of all polar atoms   =
c======================================================
      open (10, file='all-polar.txt',status='unknown')
      call system("wc -l all-polar.txt | awk '{print $1}' > line1.txt")
      open (70, file='line1.txt',status='unknown')
      read(70,*) line1
c======================================================
c     File containing water oxygen around protein     =
c     BUT NOT WITH atom index as in the original file =
c======================================================
      open (11, file='selected.txt',status='unknown')
      call system("wc -l selected.txt | awk '{print $1}' > line2.txt")
      open (70, file='line2.txt',status='unknown')
      read(70,*) line2
c======================================================
c     File containing atom-index of all water         =
c======================================================
      open (13, file='all-water.txt',status='unknown')
      call system("wc -l all-water.txt | awk '{print $1}' > line3.txt")
      open (70, file='line3.txt',status='unknown')
      read(70,*) line3
c======================================================
c     Files to be written                             =
c======================================================
      open (14, file='selected1.txt',status='unknown')
      open (50, file='top.txt',status='unknown')
      open (9, file='angle.txt',status='unknown')
c======================================================
      do a = 1,line2
        read(11,*) ind(a)
      enddo

      do a= 1,line2
       rewind 13
       do i = 1,line3
        read(13,*) atom(i), resid(i)
        if (resid(i) .eq. ind(a)) then
        write(14,*) atom(i) 
        endif
       enddo
      enddo
      close(14)

      do k = 1,line1
        read(10,*) n(k), x(k), y(k), z(k)
      enddo

c======================================================
c     File containing water oxygen around protein     =
c     WITH atom index as in the original file         =
c======================================================
      open (14, file='selected1.txt',status='unknown')
      call system("wc -l selected1.txt | awk '{print $1}' > line4.txt")
      open (70, file='line4.txt',status='unknown')
      read(70,*) line4
c======================================================
      write(*,*) line1, line2, line3, line4
      do k = 1,line4
        read(14,*) atomi(k)
      enddo

      do i= 1,line4
         do a = 1,line1
         if (n(a) .ne. atomi(i)) then
         goto 59
         else
c         write(*,*) n(a), atomi(i)
         dotp=0.0
         dotp1=0.0
         dotpx=0.0
         dotpy=0.0
         dotpz=0.0
         t=0.0
         rewind 30
         open (30, file='tmp.txt',status='unknown')
         do j=1,line1
            d(a, j) = sqrt((x(j)-x(a))**2+(y(j)-y(a))**2+(z(j)-z(a))**2)
	    write(30,*) n(j), x(j), y(j), z(j), d(a, j)        
c	    write(*,*) n(j), x(j), y(j), z(j), d(a, j)        
	 enddo
      call system('sort -nu -k 5 tmp.txt | head -n5 > nearest-four.txt')
c      call system('cat nearest-four.txt >> nearest-four_stat.txt')
         rewind 40
         open (40, file='nearest-four.txt',status='unknown')
         do m = 1,5
         read(40,*) p(m), xpos(m), ypos(m), zpos(m), r(m)
c         write(*,*) p(m), xpos(m), ypos(m), zpos(m), r(m)
         enddo
         do m = 2,4
          q=m+1
          do s= q,5
           dotpx=(xpos(m)-xpos(1))*(xpos(s)-xpos(1))
           dotpy=(ypos(m)-ypos(1))*(ypos(s)-ypos(1))
           dotpz=(zpos(m)-zpos(1))*(zpos(s)-zpos(1))
           dotp1=(dotpx+dotpy+dotpz)/((r(m)*r(s)))
           angle=acos(dotp1)
           dotp=(dotp1+0.333)**2
           t=t+dotp
           write(9,37) dotp1, angle
          enddo
         enddo
         top=1-0.375*t
         write(50,60) i, top
         endif
59    enddo
      enddo
      stop
60    FORMAT(I4, F8.4)
37    FORMAT(F8.4, F8.4)
      end
