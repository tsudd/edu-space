import React from 'react'
import { PageLayout } from '../layouts'
import { useAuth, useLogger } from '../providers'
import { TaskForm } from './TaskForm'
import { ACCESS_TOKEN_NAME, API_BASE_URL, API_TASKS } from '../constants/urls'
import { useLocation } from 'react-router'

export const TaskUpdateForm = (props) => {
  const { token } = useAuth()
  const { showError } = useLogger()
  const location = useLocation()
  console.log(location)
  const onSubmit = async (values, errors) => {
    if (Object.keys(errors).length === 0 && errors.constructor === Object) {
      showError(...Object.values(errors))
      return
    }
    new Promise((resolve) => setTimeout(() => resolve(values), 1000))
    try {
      const reps = await fetch(
        API_BASE_URL + API_TASKS + `/${location.state.task.id}`,
        {
          method: 'PUT',
          body: JSON.stringify(values),
          headers: {
            'Content-Type': 'application/json',
            Authorization: ACCESS_TOKEN_NAME + ' ' + token,
          },
        }
      )
      if (!reps.ok) {
        showError('Something went wrong.')
        return
      }
      showError('Task was updated!')
    } catch (e) {
      console.error('Ошибка:', e)
    }
  }
  return (
    <PageLayout showSubjectList={false} showMessages={false}>
      <TaskForm
        submitFunc={onSubmit}
        formTitle={`Update form`}
        task={location.state.task}
        submitTitle={'Update'}
      />
    </PageLayout>
  )
}
