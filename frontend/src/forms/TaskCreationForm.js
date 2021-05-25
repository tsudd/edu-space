import React from 'react'
import { PageLayout } from '../layouts'
import { useAuth, useLogger, useSubjects } from '../providers'
import { TaskForm } from './TaskForm'
import { ACCESS_TOKEN_NAME, API_BASE_URL, API_TASKS } from '../constants/urls'

export const TaskCreationForm = (props) => {
  const { token } = useAuth()
  const { showError } = useLogger()

  const onSubmit = async (values, errors) => {
    if (Object.keys(errors).length === 0 && errors.constructor === Object) {
      showError(...Object.values(errors))
      return
    }
    new Promise((resolve) => setTimeout(() => resolve(values), 1000))
    try {
      const reps = await fetch(API_BASE_URL + API_TASKS, {
        method: 'POST',
        body: JSON.stringify(values),
        headers: {
          'Content-Type': 'application/json',
          Authorization: ACCESS_TOKEN_NAME + ' ' + token,
        },
      })
      if (!reps.ok) {
        showError('Something went wrong.')
        return
      }
      showError('Task was created!')
    } catch (e) {
      console.error('Ошибка:', e)
    }
  }
  return (
    <PageLayout showSubjectList={false} showMessages={false}>
      <TaskForm submitFunc={onSubmit} />
    </PageLayout>
  )
}
