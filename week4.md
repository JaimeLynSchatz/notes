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