import React, { useCallback, createContext, useState, useContext } from 'react'
import { AlertComponent } from '../components/AlertComponent'

const LogContext = createContext({ showError: null })

export const useLogger = () => {
  const context = useContext(LogContext)
  if (!context) throw Error('useLogger vne providera')
  return context
}

export const LogProvider = ({ children }) => {
  const [message, setMessage] = useState('')
  const [show, setShow] = useState(false)
  const onDismiss = () => setShow(false)

  const showError = useCallback(
    (message) => {
      setMessage(message)
      setShow(true)
    },
    [setShow, setMessage]
  )

  return (
    <LogContext.Provider value={{ showError }}>
      {children}
      <AlertComponent visible={show} onDismiss={onDismiss} message={message} />
    </LogContext.Provider>
  )
}
