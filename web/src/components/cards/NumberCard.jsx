import { useEffect, useState } from "react";

function NumberCard({ cardClass, name, dataCount, dataDuration }) {
  const [displayCountValue, setDisplayCountValue] = useState(0);
  const [displayDurationValue, setDisplayDurationValue] = useState(0);

  {/* Data Count */}
  useEffect(() => {
    if (dataCount == null) return;

    const duration = 500;
    const start = performance.now();
    const from = displayCountValue;
    const to = dataCount;

    {/* Value Animation */}
    const animate = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const value = Math.round(from + (to - from) * eased);

      setDisplayCountValue(value);

      if (progress < 1) {
        requestAnimationFrame(animate);
      }
    };

    requestAnimationFrame(animate);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dataCount]);

  {/* Data Duration */}
  useEffect(() => {
    if (dataDuration == null) return;

    const duration = 500;
    const start = performance.now();
    const from = displayDurationValue;
    const to = dataDuration;

    {/* Value Animation */}
    const animate = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const value = Math.round(from + (to - from) * eased);

      setDisplayDurationValue(value);

      if (progress < 1) {
        requestAnimationFrame(animate);
      }
    };

    requestAnimationFrame(animate);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dataDuration]);

  if (dataCount === null || dataDuration === null) return <div className={cardClass}>No Data</div>;

  return (
    <div className={`${cardClass} flex flex-col justify-between`}>
      <h2 className="text-lg font-semibold mb-5">{name}</h2>

      <div className="grid grid-cols-2 gap-5 divide-x divide-base-content/10">
        {/* Count */}
        <div className="flex flex-col">
          <span className="text-sm uppercase font-semibold opacity-50 tracking-wide">
            Titles
          </span>
          <span className="text-4xl font-bold leading-tight">
            {displayCountValue.toLocaleString("fr-FR")}
          </span>
        </div>

        {/* Duration */}
        <div className="flex flex-col">
          <span className="text-sm uppercase font-semibold opacity-50 tracking-wide">
            Minutes
          </span>
          <span className="text-4xl font-bold leading-tight">
            {displayDurationValue.toLocaleString("fr-FR")}
          </span>
        </div>
      </div>
    </div>
  );
}

export default NumberCard;
