import React, { useState, useContext, useEffect } from 'react'
import {
  ACCESS_TOKEN_NAME,
  API_SUBJECTS,
  API_BASE_URL,
} from '../constants/urls'
import { useAuth } from './AuthProvider'

const SubjectsContext = React.createContext({
  subjects: null,
})

export const useSubjects = () => {
  const context = useContext(SubjectsContext)
  if (!context) throw new Error('Hook vne providera Sanya blin')
  return context
}

export const SubjectsProvider = ({ children }) => {
  const [subjects, setSubjects] = useState(null)
  const { token } = useAuth()
  useEffect(() => {
    if (!token) return
    const getSubjects = async () => {
      try {
        const resp = await fetch(API_BASE_URL + API_SUBJECTS, {
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
          setSubjects(json.subjects)
        } else {
          setSubjects(null)
        }
      } catch (e) {
        console.error(e)
      }
    }
    void getSubjects()
  }, [setSubjects, token])

  return (
    <SubjectsContext.Provider value={{ subjects }}>
      {children}
    </SubjectsContext.Provider>
  )
}
