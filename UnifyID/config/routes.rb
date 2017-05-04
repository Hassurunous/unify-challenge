Rails.application.routes.draw do
  root to: 'static_pages/home'

  get 'static_pages/randomimage'

  get 'static_pages/whitenoise'

  get 'static_pages/rsa'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
