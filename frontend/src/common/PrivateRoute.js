import React, { useEffect } from 'react'
import { Route, Redirect } from 'react-router-dom'
import { useAuth } from '../providers'

export const PrivateRoute = ({ children, ...props }) => {
  const { auth } = useAuth()
  return (
    <Route
      {...props}
      render={({ location }) =>
        auth ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: '/login',
              state: { from: location },
            }}
          />
        )
      }
    />
  )
}
