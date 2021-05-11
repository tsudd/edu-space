import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { CardBody, CardTitle, Container, Card, CardSubtitle } from 'reactstrap'
import {
  ACCESS_TOKEN_NAME,
  API_BASE_URL,
  API_SUBJECTS,
} from '../../constants/urls'

import { useAuth } from '../../providers'

export const SubjectList = (props) => {
  const [subjects, setSubjects] = useState(null)
  const { token } = useAuth()
  useEffect(() => {
    const getSubjects = async () => {
      try {
        const resp = await fetch(API_BASE_URL + API_SUBJECTS, {
          methdo: 'GET',
          headers: {
            Authorization: ACCESS_TOKEN_NAME + ' ' + token,
          },
        })
        if (resp.ok) {
          const json = await resp.json()
          setSubjects(json.subjects)
        }
      } catch (e) {
        console.error(e)
      }
    }
    void getSubjects()
  }, [setSubjects])

  return (
    <Container fluid="md">
      {subjects?.map((sub) => (
        <Link to={`/subject/${sub.id}`} key={sub.id}>
          <Card>
            <CardBody>
              <CardTitle tag="h5">{sub.name}</CardTitle>
              <CardSubtitle tag="h6" className="mb-2 text-muted">
                {sub.description}
              </CardSubtitle>
            </CardBody>
          </Card>
        </Link>
      ))}
    </Container>
  )
}
