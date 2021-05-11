import React from 'react'
// import { Router } from './Router'
import { Providers } from './providers'
import ReactDOM from 'react-dom'
import { App } from './App'

ReactDOM.render(
  <Providers>
    <App />
  </Providers>,
  document.getElementById('root')
)
