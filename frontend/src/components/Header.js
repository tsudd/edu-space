import React, { Component, useState } from 'react'
import {
  Nav,
  Navbar,
  NavbarBrand,
  NavbarToggler,
  Collapse,
  NavItem,
  Jumbotron,
} from 'reactstrap'
import { NavLink } from 'react-router-dom'
import { useAuth } from '../providers'

export const Header = (props) => {
  const [isOpen, setIsOpen] = useState(false)

  const { auth } = useAuth()

  const toggle = () => setIsOpen(!isOpen)

  //   const homeLink = null
  //   if (auth) {
  //     homeLink = (
  //       <NavItem>
  //         <NavLink className="nav-link" to="/">
  //           My Space
  //         </NavLink>
  //       </NavItem>
  //     )
  //   }

  return (
    <div>
      <Navbar color="light" light expand="md">
        <div className="container">
          <NavbarBrand className="mr-auto" href="/">
            Edu<strong>Space</strong>
          </NavbarBrand>
          <Nav navbar></Nav>
        </div>
      </Navbar>
    </div>
  )
}
