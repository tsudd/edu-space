import React, { useState } from 'react'
import { useParams } from 'react-router'
import { PageLayout } from '../../layouts'

export const Tasks = () => {
  const { id } = useParams()
  const [hide, setHide] = useState(true)
  console.log(229)
  return (
    <PageLayout showSubjectList={hide}>
      {/* <button onClick={() => setHide(!hide)}>{hide ? 'Close' : 'Open'}</button> */}
      <h1>{id}</h1>
    </PageLayout>
  )
}
