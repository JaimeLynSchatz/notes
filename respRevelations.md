After a great deal of searching and googling, I came across some interesting things about mod_tile.c

There are two different variables called `resp`

The first is a struct of the type protocol ( defined on line 192 in the request_tile function, running through until new definition on line 509)

Initially, it looks like the resp is never modified, BUT:

	When you look at a function called bzero, it uses &resp as a variable for bzero to play with.
	*****
	Is bzero() what actually asks for th tiles from the database (?? looking into that.


	Found bzero in the Linux man pages: it writes n number of 0-valued bits at location given in first argument, where n is the value of the 2nd argument ( http://man7.org/linux/man-pages/man3/bzero.3.html)


	bzero() clears the memory at that location so that it can accept from recv()  (http://man7.org/linux/man-pages/man2/recvmsg.2.html)

Later at line 509 and through, resp is used to take the http response constant (which is being defined in a http_response.h header file that is imported in, not in the main codebase - part of C? Found in http://google.github.io/google-api-cpp-client/latest/doxygen/http__types_8h_source.html)


It looks like 
