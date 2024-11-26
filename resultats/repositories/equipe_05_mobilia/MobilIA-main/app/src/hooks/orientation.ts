import { useState, useEffect } from 'react';

const useNavigation = () => {
    const [currentStep, setCurrentStep] = useState(0);
    const [route, setRoute] = useState([]);
    const [currentLocation, setCurrentLocation] = useState(null);
    const [deviceOrientation, setDeviceOrientation] = useState(null);

    useEffect(() => {
        fetchRouteData();
        requestLocationPermission();
        startLocationTracking();
        startOrientationTracking();

        return () => {
            // Clean up subscriptions when component unmounts
            navigator.geolocation.clearWatch(watchId);
            window.removeEventListener('deviceorientation', handleDeviceOrientation);
        };
    }, []);

    const fetchRouteData = async () => {
        // Fetch route data logic
    };

    const requestLocationPermission = async () => {
        if ('geolocation' in navigator) {
            const permission = await navigator.permissions.query({ name: 'geolocation' });
            if (permission.state !== 'granted') {
                alert('Location permission is required for navigation.');
            }
        } else {
            alert('Geolocation is not supported by your browser.');
        }
    };

    let watchId: any;
    const startLocationTracking = () => {
        watchId = navigator.geolocation.watchPosition(
            (position) => {
                setCurrentLocation(position.coords);
                checkNextStep(position.coords);
            },
            (error) => {
                console.error('Error getting location:', error);
            },
            { enableHighAccuracy: true, timeout: 5000, maximumAge: 0 }
        );
    };

    const startOrientationTracking = () => {
        window.addEventListener('deviceorientation', handleDeviceOrientation);
    };

    const handleDeviceOrientation = (event) => {
        const { alpha, beta, gamma } = event;
        setDeviceOrientation({ alpha, beta, gamma });
    };

    const checkNextStep = (coords) => {
        if (currentStep < route.length) {
            const nextPoint = route[currentStep].geopoint;
            const distance = calculateDistance(coords, nextPoint);
            const direction = calculateDirection(coords, nextPoint);

            if (distance < 10) { // Within 10 meters of the next point
                handleNextStep();
            } else {
                provideDirectionalGuidance(direction);
            }
        }
    };

    const calculateDistance = (point1, point2) => {
        // Haversine formula to calculate distance between two points
        // ... (implementation details omitted for brevity)
    };

    const calculateDirection = (from, to) => {
        const dx = to.longitude - from.longitude;
        const dy = to.latitude - from.latitude;
        let angle = Math.atan2(dy, dx) * 180 / Math.PI;
        if (angle < 0) {
            angle += 360;
        }
        return angle;
    };

    const provideDirectionalGuidance = (targetDirection) => {
        if (deviceOrientation) {
            const { beta, gamma } = deviceOrientation;
            const deviceHeading = Math.atan2(beta, gamma) * 180 / Math.PI;

            const relativeDirection = (targetDirection - deviceHeading + 360) % 360;

            let guidance;
            if (relativeDirection > 345 || relativeDirection <= 15) {
                guidance = "Straight ahead";
            } else if (relativeDirection > 15 && relativeDirection <= 75) {
                guidance = "Turn slight right";
            } else if (relativeDirection > 75 && relativeDirection <= 105) {
                guidance = "Turn right";
            } else if (relativeDirection > 105 && relativeDirection <= 165) {
                guidance = "Turn sharp right";
            } else if (relativeDirection > 165 && relativeDirection <= 195) {
                guidance = "Turn around";
            } else if (relativeDirection > 195 && relativeDirection <= 255) {
                guidance = "Turn sharp left";
            } else if (relativeDirection > 255 && relativeDirection <= 285) {
                guidance = "Turn left";
            } else {
                guidance = "Turn slight left";
            }

            if ('speechSynthesis' in window) {
                const utterance = new SpeechSynthesisUtterance(guidance);
                window.speechSynthesis.speak(utterance);
            } else {
                console.log('Speech synthesis not supported');
            }
        }
    };

    const handleNextStep = () => {
        // Logic to handle moving to the next step
    };

    return {
        currentStep,
        route,
        currentLocation,
        deviceOrientation,
        setRoute,
        handleNextStep,
    };
};

export default useNavigation;
