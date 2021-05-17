import React from 'react'
import { Route, BrowserRouter, Switch } from 'react-router-dom'
import { PrivateRoute } from './common/PrivateRoute'
import { Meeting } from './components/Meeting'
import { TASK_CREATION_URL, TASK_UPDATE_URL } from './constants/urls'
import { TaskCreationForm, TaskUpdateForm } from './forms'
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
          <PrivateRoute path={TASK_UPDATE_URL}>
            <TaskUpdateForm />
          </PrivateRoute>
          <PrivateRoute path={TASK_CREATION_URL}>
            <TaskCreationForm />
          </PrivateRoute>
          <PrivateRoute path="/subject/:id">
            <Tasks />
          </PrivateRoute>
          <PrivateRoute path="/">
            <Meeting />
          </PrivateRoute>
        </Switch>
      </BrowserRouter>
    </>
  )
}
