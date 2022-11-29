--
-- PostgreSQL database dump
--

-- Dumped from database version 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: albums; Type: TABLE; Schema: public; Owner: my_user
--

CREATE TABLE public.albums (
    album_id integer NOT NULL,
    title character varying,
    release_date date,
    stock integer,
    artist character varying,
    price real
);


ALTER TABLE public.albums OWNER TO my_user;

--
-- Name: albums_album_id_seq; Type: SEQUENCE; Schema: public; Owner: my_user
--

CREATE SEQUENCE public.albums_album_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.albums_album_id_seq OWNER TO my_user;

--
-- Name: albums_album_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: my_user
--

ALTER SEQUENCE public.albums_album_id_seq OWNED BY public.albums.album_id;


--
-- Name: albums album_id; Type: DEFAULT; Schema: public; Owner: my_user
--

ALTER TABLE ONLY public.albums ALTER COLUMN album_id SET DEFAULT nextval('public.albums_album_id_seq'::regclass);


--
-- Data for Name: albums; Type: TABLE DATA; Schema: public; Owner: my_user
--

COPY public.albums (album_id, title, release_date, stock, artist, price) FROM stdin;
84	macabre melodiess	2020-10-27	5	wombripper	7.2
44	storm of the light's bane	1996-10-06	4	dissection	12.9
45	the somberlain	1994-07-22	6	dissection	10.2
46	darkside	1995-01-15	2	necrophobic	9.5
47	nightmare lord	2021-02-28	10	morgal	11.4
48	tales from the morgue	2015-05-11	7	entrails	8.4
49	heavy lies the crown	2022-09-21	1	wretched path	13.5
50	kuolunkylväjä	2019-08-05	4	sielunvihollinen	10.82
\.


--
-- Name: albums_album_id_seq; Type: SEQUENCE SET; Schema: public; Owner: my_user
--

SELECT pg_catalog.setval('public.albums_album_id_seq', 86, true);


--
-- Name: albums albums_pkey; Type: CONSTRAINT; Schema: public; Owner: my_user
--

ALTER TABLE ONLY public.albums
    ADD CONSTRAINT albums_pkey PRIMARY KEY (album_id);


--
-- PostgreSQL database dump complete
--

