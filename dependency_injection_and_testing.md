#Ducks, Dependency Injection, Douglas Adams, and Testing
_Bringing it all together_

A service does one thing really well.

conquer_the_world();  // simple call, does a lot of things inside

Anything that needs to happen comes from somewhere else.
If it's external, the thing you're writing doesn't care about where it comes from.

Get 50 oz. milk
*Doesn't matter what store it comes from
*Doesn't matter if you paid cash, credit, stole it
*Doesn't matter if it's a paper or plastic container
*Or if you drove or walked, or whatever

Your interface is your surface area - what other services need _from you_

Interface: I promise those will be there

###Here's a dependency injection
private IUserService userService:

public UserController(IUserService userService)
{
	this.userService = userService;
}

Constructor-based injection === more for .NET (Unity)
Property-based injection === more for Java (Spring)

Angular === constructor based injection

Fail fast, throw an exception, all of that when there's an unfullfilled dependency.

Your component has a particular set of dependencies
