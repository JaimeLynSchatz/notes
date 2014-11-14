# Notes from StackOverflow

Route root will not work with whole controller as this has to point on specific action.

First parameter of resources will be used to determine path (normally it would be /notes) and at the same time to create helpers like notes_path. What you want to do is set this to '/', but also add :as option to give proper helpers names. So finally it should look like:

resources '/', controller: :notes, as: :notes
Also quite important thing to notice, if you want to use any other resources, you should put them above notes route. Otherwise rails will recognize resources name as id of notes action show.

Example:

resources '/', controller: :notes, as: :notes
resources :comments
Going to /comments will try to find note with id 'comments'.

resources :comments
resources '/', controller: :notes, as: :notes
Opening /comments will go to comments_controller#index.

# More
As far as I know

match '/something', :to => 'pages#something'
match '/something' => 'pages#something'
are equivalent. It isn't uncommon to find more than one way to say the same thing in Rails. Shorthand notation abounds for commonly used methods. If you care, the latter is what I use and see more often.

As far as the root route is concerned, here is what is going on: root :to => 'pages#home' is mapping "/" to the home method in pages_controller.rb, as you already know. But using "pages#home" does not create the url "pages/home". All it does is tell rails what to execute when it encounters "/". That is why you need to also tell rails what to do when it encounters "pages/home". Route definitions are a one-way deal.

# Another Rails Guide [http://guides.rubyonrails.org/routing.html]
1.2 Generating Paths and URLs from Code
You can also generate paths and URLs. If the route above is modified to be:

get '/patients/:id', to: 'patients#show', as: 'patient'
and your application contains this code in the controller:

@patient = Patient.find(17)
and this in the corresponding view:

<%= link_to 'Patient Record', patient_path(@patient) %>
then the router will generate the path /patients/17. This reduces the brittleness of your view and makes your code easier to understand. Note that the id does not need to be specified in the route helper.