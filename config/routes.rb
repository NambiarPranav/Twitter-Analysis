Rails.application.routes.draw do
  get 'static/home'

  get '/imagetext', to: 'static#imagetext'

  get '/retweet', to: 'static#retweet'

  get '/mentions', to: 'static#mentions'

  get '/topten', to: 'static#topten'

  get '/favorite', to: 'static#favorite'

  root 'static#home'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
