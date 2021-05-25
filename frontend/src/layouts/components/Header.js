import React, { useState, useEffect } from 'react'
import { Nav, Navbar, NavbarBrand, NavItem, NavLink } from 'reactstrap'
import { Link, useHistory } from 'react-router-dom'
import { useAuth } from '../../providers'
import {
  ACCESS_TOKEN_NAME,
  MESSAGE_CREATION_URL,
  TASK_CREATION_URL,
} from '../../constants/urls'

export const Header = (props) => {
  const { auth, setAuth, user, setUser, setToken } = useAuth()
  let logout
  let history = useHistory()
  let staff_links

  const handleLogout = () => {
    localStorage.removeItem(ACCESS_TOKEN_NAME)
    setAuth(false)
    setUser(null)
    setToken(null)
  }

  if (auth) {
    logout = (
      <NavItem>
        <Link className="nav-link mt-2" to="/login" onClick={handleLogout}>
          Logout
        </Link>
      </NavItem>
    )
  }
  if (auth && user && user.is_staff) {
    staff_links = [
      <NavItem key="0">
        <Link className="nav-link mt-2" to={TASK_CREATION_URL}>
          Create task
        </Link>
      </NavItem>,
      <NavItem key="1">
        <Link className="nav-link mt-2" to={MESSAGE_CREATION_URL}>
          Create message
        </Link>
      </NavItem>,
    ]
  }

  return (
    <div>
      <Navbar color="light" light expand="md">
        <div className="container">
          <Link className="mr-auto navbar-brand" to="/">
            Edu<strong>Space</strong>
          </Link>
          <Nav navbar>
            <NavItem>
              <a
                className="nav-link p-2"
                href="https://github.com/tsudd/edu-space"
                target="_blank"
                rel="noopener"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="36"
                  height="36"
                  className="navbar-nav-svg d-inline-block align-text-top"
                  viewBox="0 0 512 499.36"
                  role="img"
                >
                  <title>GitHub</title>
                </svg>
                <small className="d-md-none ms-2">GitHub</small>
              </a>
            </NavItem>
            {logout}
            {staff_links?.map((link) => {
              return link
            })}
          </Nav>
        </div>
      </Navbar>
    </div>
  )
}
