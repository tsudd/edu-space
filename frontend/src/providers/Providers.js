import React from 'react'

import { AuthProvider } from './AuthProvider'

export const Providers = ({ children }) => {
  return <AuthProvider>{children}</AuthProvider>
}
