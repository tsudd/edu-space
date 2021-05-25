import React, { useState, useContext, useEffect } from 'react'
import {
  ACCESS_TOKEN_NAME,
  API_BASE_URL,
  API_MESSAGES,
} from '../constants/urls'
import { useAuth } from './AuthProvider'

const MessagesContext = React.createContext({
  messages: null,
})

export const useMessages = () => {
  const context = useContext(MessagesContext)
  if (!context) throw new Error('Hook vne providera Sanya blin')
  return context
}

export const MessagesProvider = ({ children }) => {
  const [messages, setMessages] = useState(null)
  const { token } = useAuth()
  useEffect(() => {
    if (!token) return
    const getMessages = async () => {
      try {
        const resp = await fetch(API_BASE_URL + API_MESSAGES, {
          methdo: 'GET',
          headers: {
            Authorization: ACCESS_TOKEN_NAME + ' ' + token,
          },
        })
        if (resp.status == 204) {
          return
        }
        if (resp.ok) {
          const json = await resp.json()
          setMessages(json.messages)
        } else {
          setMessages(null)
        }
      } catch (e) {
        console.error(e)
      }
    }
    void getMessages()
  }, [setMessages, token])

  return (
    <MessagesContext.Provider value={{ messages, setMessages }}>
      {children}
    </MessagesContext.Provider>
  )
}
