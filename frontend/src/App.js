import React from 'react'
import { Route, BrowserRouter, Switch } from 'react-router-dom'
import { PrivateRoute } from './common/PrivateRoute'
import { Meeting } from './components/Meeting'
import { PageLayout } from './layouts'
import { Login } from './modules/auth/Login'
import { Tasks } from './modules/tasks/Tasks'

export const App = () => {
  return (
    <>
      <BrowserRouter>
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <PrivateRoute path="/">
            <Meeting></Meeting>
          </PrivateRoute>
          <PrivateRoute path="/subject/:id">
            <Tasks />
          </PrivateRoute>
        </Switch>
      </BrowserRouter>
    </>
  )
}
