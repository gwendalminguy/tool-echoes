import { createContext, useContext, useState, useEffect } from "react";

const StatisticsContext = createContext();

export function StatisticsProvider({ year, children }) {
  const [statistics, setStatistics] = useState(null);
  const [loading, setLoading] = useState(true);

  const [prev, setPrev] = useState(false);
  const [next, setNext] = useState(false);

  useEffect(() => {
    fetch(`/exports/${year}.json?t=${Date.now()}`)
      .then((r) => r.json())
      .then(setStatistics)
      .finally(() => setLoading(false));
  }, [year]);

  useEffect(() => {
    const prevYear = year - 1;
    const nextYear = year + 1;

    const checkExists = (y, setter) => {
      fetch(`/exports/${y}.json`, { method: "HEAD" })
        .then((res) => setter(res.ok))
        .catch(() => setter(false));
    };

    checkExists(prevYear, setPrev);
    checkExists(nextYear, setNext);
  }, [year]);

  return (
    <StatisticsContext.Provider value={{ statistics, loading, prev, next }}>
      {children}
    </StatisticsContext.Provider>
  );
}

export function useStatistics() {
  return useContext(StatisticsContext);
}
