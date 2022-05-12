import React, { useState } from "react";
import { Modal } from "../../context/Modal";
import LoginForm from "../auth/LoginForm";
import SignUpForm from "../auth/SignUpForm";
import SplashBanner from "./SplashBanner";
import SplashHeader from "./SplashHeader";
import './SplashPage.css';

const SplashPage = () => {
    return (
        <div className="page-container">
            <header className="bounded-1200 centered fixed">
                <SplashHeader />
            </header>
            <main>
                <SplashBanner />
            </main>
        </div>
    )
};

export default SplashPage;
