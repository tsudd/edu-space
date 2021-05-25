import React from 'react'

import { AuthProvider } from './AuthProvider'
import { LogProvider } from './LogProvider'
import { MessagesProvider } from './MessagesProvider'
import { SubjectsProvider } from './SubjectsProvider'

export const Providers = ({ children }) => {
  return (
    <LogProvider>
      <AuthProvider>
        <SubjectsProvider>
          <MessagesProvider>{children}</MessagesProvider>
        </SubjectsProvider>
      </AuthProvider>
    </LogProvider>
  )
}
