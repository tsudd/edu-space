import React from 'react'

import { AuthProvider } from './AuthProvider'
import { LogProvider } from './LogProvider'

export const Providers = ({ children }) => {
  return (
    <LogProvider>
      <AuthProvider>{children}</AuthProvider>
    </LogProvider>
  )
}
