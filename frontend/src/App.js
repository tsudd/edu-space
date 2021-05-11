import React, { useState } from 'react'
import { useAuth } from './providers'
import { Route, BrowserRouter, Switch, useHistory } from 'react-router-dom'
import { PrivateRoute } from './common/PrivateRoute'
import { Login } from './auth/Login'
import { Header } from './components/Header'
import { AlertComponent } from './components/AlertComponent'
import { Main } from './components/Main'

export const App = () => {
  const { auth, token, user } = useAuth()

  let history = useHistory()
  const [errorMessage, updateErrorMessage] = useState(null)

  return (
    <div>
      <BrowserRouter>
        <Header />
        <Switch>
          <Route path="/login">
            <Login showError={updateErrorMessage} />
          </Route>
          <PrivateRoute path="/">
            <Main />
          </PrivateRoute>
        </Switch>
      </BrowserRouter>
      <AlertComponent
        errorMessage={errorMessage}
        hideError={updateErrorMessage}
      />
    </div>
  )
}
