import React from 'react'

import { AuthProvider } from './AuthProvider'
import { LogProvider } from './LogProvider'
import { SubjectsProvider } from './SubjectsProvider'

export const Providers = ({ children }) => {
  return (
    <LogProvider>
      <AuthProvider>
        <SubjectsProvider>{children}</SubjectsProvider>
      </AuthProvider>
    </LogProvider>
  )
}
