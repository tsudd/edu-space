import React, { useEffect } from 'react'
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom'
import { useAuth } from './providers'

const Login = () => {
  const { setAuth, auth } = useAuth()
  useEffect(() => {
    setTimeout(() => {
      setAuth(true)
    }, 1000)
  }, [])

  if (auth) return <Redirect to="/" />

  return <h1>Login...</h1>
}

export const Router = () => {
  const { auth } = useAuth()
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/login" component={Login} />
        <Route path="/">
          {!auth ? <Redirect to="/login" /> : <AccountsList />}
        </Route>
      </Switch>
    </BrowserRouter>
  )
}
