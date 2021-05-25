import React from 'react'
import {
  Card,
  Col,
  CardBody,
  CardTitle,
  Button,
  Form,
  FormGroup,
  Label,
  Input,
} from 'reactstrap'
import { Formik } from 'formik'
import { useAuth, useLogger, useSubjects } from '../providers'
import { object, string } from 'yup'
import { PageLayout } from '../layouts/PageLayout'
import {
  API_MESSAGES,
  API_BASE_URL,
  ACCESS_TOKEN_NAME,
} from '../constants/urls'

const initialValues = {
  class_receiver: '',
  text: '',
}

const validationSchema = object({
  class_receiver: string().required('Choose class receiver'),
  text: string().required("You can't send blank messages"),
})

export const MessageCreateForm = () => {
  const { subjects } = useSubjects()
  const { token, user } = useAuth()
  const { showError } = useLogger()

  const onSubmit = async (values, errors) => {
    if (Object.keys(errors).length === 0 && errors.constructor === Object) {
      showError(...Object.values(errors))
      return
    }
    new Promise((resolve) => setTimeout(() => resolve(values), 1000))
    try {
      const reps = await fetch(API_BASE_URL + API_MESSAGES, {
        method: 'POST',
        body: JSON.stringify({
          ...values,
          sender: user.id,
          creation_datetime: moment().format(),
        }),
        headers: {
          'Content-Type': 'application/json',
          Authorization: ACCESS_TOKEN_NAME + ' ' + token,
        },
      })
      if (!reps.ok) {
        showError('Something went wrong.')
        return
      }
      showError('Message was sended!')
    } catch (e) {
      console.error('Ошибка:', e)
    }
  }
  const classes = subjects?.map((sub) => {
    return sub.stud_class
  })

  return (
    <PageLayout showMessages={false} showSubjectList={false}>
      <Col md="9" className="mx-auto mt-5">
        <Card>
          <CardBody>
            <CardTitle tag="h5">Message creation</CardTitle>
            <Formik
              onSubmit={onSubmit}
              validationSchema={validationSchema}
              initialValues={initialValues}
            >
              {({
                values,
                errors,
                handleChange,
                handleSubmit,
                isSubmitting,
                handleBlur,
              }) => (
                <Form onSubmit={(e) => e.preventDefault()}>
                  <FormGroup>
                    <Label>Class receiver</Label>
                    <Col sm={10}>
                      {classes?.map((sub) => (
                        <FormGroup check key={sub.id}>
                          <Label check>
                            <Input
                              type="radio"
                              name={'class_receiver'}
                              value={sub.id}
                              onChange={handleChange}
                              onBlur={handleBlur}
                              invalid={!!errors.subject}
                            />{' '}
                            {sub.number} | {sub.letter}
                          </Label>
                        </FormGroup>
                      ))}
                    </Col>
                  </FormGroup>
                  <FormGroup>
                    <Label for="description">Message text</Label>
                    <Input
                      type="textarea"
                      name="text"
                      onBlur={handleBlur}
                      invalid={!!errors.description}
                      value={values.description}
                      id="text"
                      placeholder="Enter information here"
                      onChange={handleChange}
                    />
                  </FormGroup>
                  <FormGroup>
                    <Button
                      type="submit"
                      color="primary"
                      disabled={isSubmitting}
                      onClick={handleSubmit}
                    >
                      Send
                    </Button>
                  </FormGroup>
                </Form>
              )}
            </Formik>
          </CardBody>
        </Card>
      </Col>
    </PageLayout>
  )
}
